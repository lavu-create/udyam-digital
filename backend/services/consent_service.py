import hashlib
from datetime import datetime
from typing import Dict, Any, Optional
from backend.database import SessionLocal
from backend.models.orm import ConsentRecord, AuditLog

class ConsentService:
    def record_consent(
        self,
        purpose: str = "TELECOM_STATUTORY_PROVISIONING",
        language: str = "en",
        business_id: Optional[int] = None,
        order_id: Optional[str] = None,
        client_ip: str = "127.0.0.1"
    ) -> Dict[str, Any]:
        ip_hash = hashlib.sha256(client_ip.encode()).hexdigest()
        now = datetime.utcnow()

        db = SessionLocal()
        try:
            record = ConsentRecord(
                business_id=business_id,
                order_id=order_id,
                purpose=purpose,
                language=language,
                ip_hash=ip_hash,
                accepted_at=now,
                terms_version="1.0-DPDP2023"
            )
            db.add(record)
            db.commit()
            db.refresh(record)

            # Audit log
            audit = AuditLog(
                entity_type="CONSENT",
                entity_id=str(record.id),
                action="AFFIRMATIVE_CONSENT_CAPTURED",
                details=f"Purpose: {purpose}, Language: {language}, IP_Hash: {ip_hash[:8]}...",
                timestamp=now
            )
            db.add(audit)
            db.commit()

            audit_token = f"DPDP-{record.id}-{ip_hash[:12]}"
            return {
                "success": True,
                "consent_id": record.id,
                "timestamp": now.isoformat() + "Z",
                "language": language,
                "audit_hash": audit_token
            }
        finally:
            db.close()

consent_service = ConsentService()

