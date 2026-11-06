import csv
import os
from typing import List, Dict, Any, Tuple
from backend.config import CATALOGUE_CSV

class CatalogService:
    def __init__(self):
        self.products: Dict[str, Dict[str, Any]] = {}
        self.load_catalogue()

    def load_catalogue(self):
        if not os.path.exists(CATALOGUE_CSV):
            raise FileNotFoundError(f"Catalogue CSV not found at: {CATALOGUE_CSV}")

        with open(CATALOGUE_CSV, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                pid = row["product_id"].strip()
                self.products[pid] = {
                    "product_id": pid,
                    "category": row["category"].strip(),
                    "product_name": row["product_name"].strip(),
                    "description": row["description"].strip(),
                    "unit": row["unit"].strip(),
                    "price_min_inr_per_month": float(row["price_min_inr_per_month"]),
                    "price_max_inr_per_month": float(row["price_max_inr_per_month"]),
                    "one_time_setup_inr": float(row["one_time_setup_inr"]) if row["one_time_setup_inr"] else 0.0,
                    "min_contract_months": int(row["min_contract_months"]) if row["min_contract_months"] else 12,
                    "available_city_tiers": row["available_city_tiers"].strip(),
                    "min_employees": int(row["min_employees"]) if row["min_employees"] else 1,
                    "min_sites": int(row["min_sites"]) if row["min_sites"] else 1,
                    "requires_gstin": row["requires_gstin"].strip().upper(),
                    "requires_one_of": row["requires_one_of"].strip() if row["requires_one_of"] else None,
                    "typical_install_days": int(row["typical_install_days"]) if row["typical_install_days"] else 5,
                    "target_segments": row["target_segments"].strip() if row["target_segments"] else "",
                }

    def get_all_products(self) -> List[Dict[str, Any]]:
        return list(self.products.values())

    def get_product(self, product_id: str) -> Dict[str, Any]:
        return self.products.get(product_id)

    def validate_and_quote(
        self,
        product_ids: List[str],
        has_active_gstin: bool = False,
        site_count: int = 1,
        employee_count: int = 5
    ) -> Dict[str, Any]:
        errors = []
        warnings = []
        items = []
        
        monthly_total_min = 0.0
        monthly_total_max = 0.0
        setup_fee_total = 0.0
        requires_gstin_flag = False

        selected_set = set(product_ids)

        for pid in product_ids:
            p = self.get_product(pid)
            if not p:
                errors.append(f"Invalid product code '{pid}'.")
                continue

            # GSTIN statutory check
            if p["requires_gstin"] == "Y":
                requires_gstin_flag = True

            # Product Dependency Check
            if p["requires_one_of"]:
                allowed_deps = [dep.strip() for dep in p["requires_one_of"].split("|") if dep.strip()]
                if not any(dep in selected_set for dep in allowed_deps):
                    dep_names = [self.get_product(d)["product_name"] for d in allowed_deps if self.get_product(d)]
                    errors.append(
                        f"Product '{p['product_name']}' ({pid}) requires at least one base connection: "
                        f"{', '.join(dep_names)} ({p['requires_one_of']})."
                    )

            # Minimum requirements warnings
            if employee_count < p["min_employees"]:
                warnings.append(
                    f"'{p['product_name']}' is typically designed for >= {p['min_employees']} staff."
                )
            if site_count < p["min_sites"]:
                warnings.append(
                    f"'{p['product_name']}' is recommended for multi-site setups (>= {p['min_sites']} locations)."
                )

            # Multiply per site/user if applicable
            monthly_total_min += p["price_min_inr_per_month"]
            monthly_total_max += p["price_max_inr_per_month"]
            setup_fee_total += p["one_time_setup_inr"]

            items.append({
                "product_id": pid,
                "product_name": p["product_name"],
                "category": p["category"],
                "price_min": p["price_min_inr_per_month"],
                "price_max": p["price_max_inr_per_month"],
                "setup_fee": p["one_time_setup_inr"]
            })

        gstin_satisfied = True
        if requires_gstin_flag and not has_active_gstin:
            gstin_satisfied = False
            errors.append(
                "One or more enterprise SKUs in your selection require an Active GSTIN registration."
            )

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "monthly_total_min": round(monthly_total_min, 2),
            "monthly_total_max": round(monthly_total_max, 2),
            "setup_fee_total": round(setup_fee_total, 2),
            "requires_gstin": requires_gstin_flag,
            "gstin_satisfied": gstin_satisfied,
            "items": items
        }

catalog_service = CatalogService()

