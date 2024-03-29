from django.contrib import admin
from .models import Locations
from .models import BarInventory
from .models import Bartables
from .models import Branches
from .models import EmployeePosition
from .models import Employees
from .models import FeedbackReviews
from .models import Guesses
from .models import Membership
from .models import Reservations
from .models import SecurityLogs
from .models import Orders
from .models import OrderProduct


# Register your models here.
admin.site.register(Locations)
admin.site.register(BarInventory)
admin.site.register(Bartables)
admin.site.register(Branches)
admin.site.register(EmployeePosition)
admin.site.register(Employees)
admin.site.register(FeedbackReviews)
admin.site.register(Guesses)
admin.site.register(Membership)
admin.site.register(Reservations)
admin.site.register(SecurityLogs)
admin.site.register(Orders)
admin.site.register(OrderProduct)

