#modify the config file with puppet
file { '/root/.ssh/config':
  ensure  => file,
  mode    => '0600',
  content => "Host 34.202.159.232\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",  
}
