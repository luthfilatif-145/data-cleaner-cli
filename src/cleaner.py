from typing import Any, Dict, List, Optional, Tuple
from pydantic import ValidationError
from src.schema import UserDataSchema

def clean_and_validate_row(raw_data: Dict[str, Any]) -> Tuple[Optional[Dict[str, Any]], List[str]]:
    errors: List[str] = []
    
    # 1. Edge Case: Check empty payload
    if not raw_data:
        return None, ["Payload data kosong"]

    # 2. Sanitasi String (Trim whitespace)
    sanitized_data = {}
    for key, value in raw_data.items():
        if isinstance(value, str):
            sanitized_data[key] = value.strip()
        else:
            sanitized_data[key] = value

    # 3. Validasi via Pydantic Schema
    try:
        validated_obj = UserDataSchema(**sanitized_data)
        return validated_obj.model_dump(), []
    except ValidationError as e:
        for err in e.errors():
            field = ".".join(str(loc) for loc in err["loc"])
            errors.append(f"Field '{field}': {err['msg']}")
        return None, errors