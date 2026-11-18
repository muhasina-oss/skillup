from rest_framework.permissions import BasePermission


class IsTrainer(BasePermission):
  
  def has_object_permission(self, request, view, obj):
    
    return obj.trainer==request.user