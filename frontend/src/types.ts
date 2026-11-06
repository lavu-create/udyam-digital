export interface Product {
  product_id: string;
  category: string;
  product_name: string;
  description: string;
  unit: string;
  price_min_inr_per_month: number;
  price_max_inr_per_month: number;
  one_time_setup_inr: number;
  min_contract_months: number;
  available_city_tiers: string;
  min_employees: number;
  min_sites: number;
  requires_gstin: string;
  requires_one_of?: string;
  typical_install_days: number;
  target_segments: string;
}

export interface Bundle {
  tier: string;
  title: string;
  badge: string;
  monthly_price: number;
  description: string;
  product_ids: string[];
  highlights: string[];
}

export interface QuoteValidation {
  valid: boolean;
  errors: string[];
  warnings: string[];
  monthly_total_min: number;
  monthly_total_max: number;
  setup_fee_total: number;
  requires_gstin: boolean;
  gstin_satisfied: boolean;
  items: Array<{
    product_id: string;
    product_name: string;
    category: string;
    price_min: number;
    price_max: number;
    setup_fee: number;
  }>;
}

export interface Milestone {
  milestone: string;
  title: string;
  status: 'COMPLETED' | 'IN_PROGRESS' | 'PENDING';
  notes: string;
  completed_at?: string;
}

export interface OrderState {
  order_id: string;
  status: string;
  business_name: string;
  installation_address: string;
  monthly_recurring_inr: number;
  setup_fee_inr: number;
  technician_name: string;
  technician_phone: string;
  scheduled_install_date: string;
  milestones: Milestone[];
}
