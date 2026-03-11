from pydantic import BaseModel
from typing import Optional

class UserAccountContext(BaseModel):
    
    customer_id: int
    name: str
    tier: str = "basic" 
    email: Optional[str] = None #premium enterprise type이 있을 수도 없을수도 있는 Optional
    
class InputGuardRailOutput(BaseModel):
    
    is_off_topic: bool
    reason: str

class TechnicalOutputGuardRailOutput(BaseModel):
    
    contain_off_topic: bool
    contain_billing_data: bool
    contain_account_data: bool
    reason: str
    
    0
class HandoffData(BaseModel):
    
    to_agent_name: str
    issue_type: str
    issue_description: str
    reason: str
    
    