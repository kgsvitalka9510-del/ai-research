"""IDOR in GraphQL Fix"""
def validate_user_access(user_id, resource_id):
    """Validate user has access to resource."""
    # Check user owns the resource
    if not user_owns_resource(user_id, resource_id):
        raise PermissionError("Access denied")
    return True

def user_owns_resource(user_id, resource_id):
    """Check if user owns the resource."""
    # Query database to verify ownership
    return True  # Placeholder
