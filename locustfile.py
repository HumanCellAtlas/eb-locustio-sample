from locust import HttpLocust

# from locustfiles.common.dsslocust import DSSLocust
# from locustfiles import UploadTaskSet, NotifyTaskSet, SearchTaskSet, DownloadTaskSet, CheckoutTaskSet
from locustfiles import SearchTaskSet

# class UploadUser(DSSLocust):
#     min_wait = 1000
#     max_wait = 3000
#     task_set = UploadTaskSet
#     weight = 1
#
#
# class CheckoutUser(DSSLocust):
#     min_wait = 3000
#     max_wait = 3000
#     task_set = CheckoutTaskSet
#     weight = 3
#
#
# class DownloadUser(DSSLocust):
#     min_wait = 500
#     max_wait = 1000
#     task_set = DownloadTaskSet
#     weight = 3
#
#
# class NotifiedUser(DSSLocust):
#     min_wait = 1000
#     max_wait = 3000
#     task_set = NotifyTaskSet
#     weight = 2


class SearchUser(HttpLocust):
    min_wait = 250
    max_wait = 500
    task_set = SearchTaskSet
    weight = 4
