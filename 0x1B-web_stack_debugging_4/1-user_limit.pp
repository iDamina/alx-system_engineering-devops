# reconfiguring the OS of Holberton to login and open a file without an error message

exec { 'increase-hard-file-limit-holberton-user':
  command => 'sed -i "/holberton hard/s/4/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/5/5000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
