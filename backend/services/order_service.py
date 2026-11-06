import random
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from backend.database import SessionLocal
from backend.models.orm import Order, OrderMilestone, AuditLog

class OrderService:
    MILESTONES_FLOW = [
        ("KYC_VERIFIED", "Digital KYC & Registry Verification Cleared", "Completed automated verification against synthetic GSTIN & Udyam test registries."),
        ("FEASIBILITY_CLEARED", "Site Optical & Radio Feasibility Cleared", "Simulated local Airtel OLT distribution point allocation."),
        ("EQUIPMENT_DISPATCHED", "Airtel Wi-Fi 6 Router & CPE Dispatched", "Simulated CPE kit assignment from regional demonstration inventory."),
        ("INSTALLATION_SCHEDULED", "Technician Appointment Confirmed", "Simulated field technician scheduled for on-premise demonstration drop."),
        ("SERVICE_ACTIVE", "Service Provisioned & Live", "Active optical link established; high-speed simulated throughput verified.")
    ]

    def create_order(
        self,
        product_ids: List[str],
        business_name: str,
        contact_name: str,
        contact_phone: str,
        installation_address: str,
        monthly_price: float,
        setup_fee: float = 0.0,
        quote_id: Optional[str] = None,
        gstin: Optional[str] = None,
        udyam_number: Optional[str] = None
    ) -> Dict[str, Any]:
        db = SessionLocal()
        try:
            rand_suffix = random.randint(1000, 9999)
            order_id = f"ORD-2026-{rand_suffix}"
            now = datetime.utcnow()
            install_date = (now + timedelta(days=3)).strftime("%d %B %Y, 11:00 AM (Simulated)")

            order = Order(
                id=order_id,
                quote_id=quote_id or f"Q-{rand_suffix}",
                status="FEASIBILITY_CLEARED",
                monthly_recurring_inr=monthly_price,
                setup_fee_inr=setup_fee,
                technician_name="Simulated Field Tech (Demo Node #402)",
                technician_phone="+91 98000 00000 (Demo)",
                scheduled_install_date=install_date,
                created_at=now,
                updated_at=now
            )
            db.add(order)

            # Create default milestones
            milestones = []
            for idx, (code, title, desc) in enumerate(self.MILESTONES_FLOW):
                if idx <= 1:
                    m_status = "COMPLETED"
                    comp_time = now - timedelta(hours=2 - idx)
                elif idx == 2:
                    m_status = "IN_PROGRESS"
                    comp_time = None
                else:
                    m_status = "PENDING"
                    comp_time = None

                m_record = OrderMilestone(
                    order_id=order_id,
                    milestone=code,
                    status=m_status,
                    completed_at=comp_time,
                    notes=desc
                )
                db.add(m_record)
                milestones.append({
                    "milestone": code,
                    "title": title,
                    "status": m_status,
                    "notes": desc,
                    "completed_at": comp_time.isoformat() + "Z" if comp_time else None
                })

            db.commit()

            return {
                "order_id": order_id,
                "status": order.status,
                "business_name": business_name,
                "installation_address": installation_address,
                "monthly_recurring_inr": monthly_price,
                "setup_fee_inr": setup_fee,
                "technician_name": order.technician_name,
                "technician_phone": order.technician_phone,
                "scheduled_install_date": install_date,
                "milestones": milestones
            }
        finally:
            db.close()

    def get_order(self, order_id: str) -> Optional[Dict[str, Any]]:
        db = SessionLocal()
        try:
            order = db.query(Order).filter(Order.id == order_id).first()
            if not order:
                return None

            m_records = db.query(OrderMilestone).filter(OrderMilestone.order_id == order_id).all()
            milestones = []
            title_map = {code: title for code, title, _ in self.MILESTONES_FLOW}
            for m in m_records:
                milestones.append({
                    "milestone": m.milestone,
                    "title": title_map.get(m.milestone, m.milestone),
                    "status": m.status,
                    "notes": m.notes,
                    "completed_at": m.completed_at.isoformat() + "Z" if m.completed_at else None
                })

            return {
                "order_id": order.id,
                "status": order.status,
                "business_name": "Demo Applicant Business",
                "installation_address": "Premises Site Address [Demonstration]",
                "monthly_recurring_inr": order.monthly_recurring_inr,
                "setup_fee_inr": order.setup_fee_inr,
                "technician_name": order.technician_name or "Simulated Field Tech (Demo Node #402)",
                "technician_phone": order.technician_phone or "+91 98000 00000 (Demo)",
                "scheduled_install_date": order.scheduled_install_date,
                "milestones": milestones
            }
        finally:
            db.close()

    def advance_order(self, order_id: str) -> Optional[Dict[str, Any]]:
        db = SessionLocal()
        try:
            order = db.query(Order).filter(Order.id == order_id).first()
            if not order:
                return None

            m_records = db.query(OrderMilestone).filter(OrderMilestone.order_id == order_id).order_id_asc() if hasattr(OrderMilestone, 'order_id_asc') else db.query(OrderMilestone).filter(OrderMilestone.order_id == order_id).all()
            
            # Find first non-completed milestone
            advanced = False
            for m in m_records:
                if m.status != "COMPLETED":
                    m.status = "COMPLETED"
                    m.completed_at = datetime.utcnow()
                    order.status = m.milestone
                    order.updated_at = datetime.utcnow()
                    advanced = True
                    break

            if advanced:
                db.commit()

            return self.get_order(order_id)
        finally:
            db.close()

order_service = OrderService()

