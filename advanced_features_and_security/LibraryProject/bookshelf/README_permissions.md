Permissions and Groups Setup

Custom permissions added to Book model:
- can_view
- can_create
- can_edit
- can_delete

Groups created in Django admin:

Viewers → can_view  
Editors → can_view, can_create, can_edit  
Admins → can_view, can_create, can_edit, can_delete  

Views are protected using @permission_required decorator.
Users must belong to the correct group to access views.
