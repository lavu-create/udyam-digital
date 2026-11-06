import csv
import os
from typing import Dict, Any, Optional
from backend.config import GSTIN_REGISTRY_CSV, UDYAM_REGISTRY_CSV

class RegistryService:
    def __init__(self):
        self.gstin_index: Dict[str, Dict[str, Any]] = {}
        self.udyam_index: Dict[str, Dict[str, Any]] = {}
        self.load_registries()

    def load_registries(self):
        if os.path.exists(GSTIN_REGISTRY_CSV):
            with open(GSTIN_REGISTRY_CSV, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    g = row["gstin"].strip().upper()
                    self.gstin_index[g] = {
                        "gstin": g,
                        "legal_name": row["legal_name"].strip(),
                        "trade_name": row["trade_name"].strip(),
                        "constitution": row["constitution"].strip(),
                        "principal_place_of_business": row["principal_place_of_business"].strip(),
                        "state": row["state"].strip(),
                        "registration_date": row["registration_date"].strip(),
                        "status": row["status"].strip()  # Active, Cancelled, Suspended
                    }

        if os.path.exists(UDYAM_REGISTRY_CSV):
            with open(UDYAM_REGISTRY_CSV, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    u = row["udyam_number"].strip().upper()
                    self.udyam_index[u] = {
                        "udyam_number": u,
                        "enterprise_name": row["enterprise_name"].strip(),
                        "enterprise_type": row["enterprise_type"].strip(),
                        "major_activity": row["major_activity"].strip(),
                        "nic_description": row["nic_description"].strip(),
                        "state": row["state"].strip(),
                        "city": row["city"].strip(),
                        "date_of_registration": row["date_of_registration"].strip()
                    }

    def lookup_gstin(self, gstin: str) -> Dict[str, Any]:
        key = gstin.strip().upper()
        if key in self.gstin_index:
            entry = self.gstin_index[key]
            return {
                "found": True,
                "registry": "GSTIN",
                "status": entry["status"],
                "legal_name": entry["legal_name"],
                "trade_name": entry["trade_name"],
                "address": entry["principal_place_of_business"],
                "registration_date": entry["registration_date"],
                "details": entry
            }
        return {
            "found": False,
            "registry": "GSTIN",
            "status": "NOT_FOUND",
            "details": {}
        }

    def lookup_udyam(self, udyam_number: str) -> Dict[str, Any]:
        key = udyam_number.strip().upper()
        if key in self.udyam_index:
            entry = self.udyam_index[key]
            return {
                "found": True,
                "registry": "UDYAM",
                "status": "Active",
                "legal_name": entry["enterprise_name"],
                "trade_name": entry["enterprise_name"],
                "address": f"{entry['city']}, {entry['state']}",
                "registration_date": entry["date_of_registration"],
                "details": entry
            }
        return {
            "found": False,
            "registry": "UDYAM",
            "status": "NOT_FOUND",
            "details": {}
        }

registry_service = RegistryService()

