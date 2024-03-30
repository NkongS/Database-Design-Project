from .models import Branches

def branch_name(request):
    branch_name = ''
    if 'branch' in request.path:
        try:
            branch_id = request.path.split('/')[2]
            branch = Branches.objects.get(branch_id=branch_id)
            branch_name = branch.branch_name
        except (Branches.DoesNotExist, ValueError, IndexError):
            pass
    return {'branch_name': branch_name}