pi-ph
=====


doc links
---------
http://www.sparkyswidgets.com/portfolio-item/leophi-usb-arduino-ph-sensor/


setup
-----

* Give user access to the serial port

    ls -l /dev/ttyACM0

*  Check the group access and grant this group to your user

    usermod -G <group> -a <user>

* Logout and login again. Check to see that you have the relevant group permissions

    $ id
    uid=1001(serial_user) gid=1001(serial_user) groups=1001(serial_user),20(dialout)
