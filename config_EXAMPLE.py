# rename to config.py before running notify.py

pushsafer_api_key = 'yourapikeyhere'
# register at https://www.pushsafer.com/ for 50 free mobile push notifications
notify_via_pushsafer = False
# if True attempt to send a notification to your iOS/Android devices via pushover
notify_via_macos = True
# if True send a notification (MacOS only)

#
# Get RiteAid store numbers at the store locator https://www.riteaid.com/locations/search.html
close_stores = ['1711']
# List of most preferred stores (closest to you). Pushsafer notifications will only happen for one of these stores
far_stores = ['3711', '4205']
# Secondary stores will still get logged and MacOS notifications
