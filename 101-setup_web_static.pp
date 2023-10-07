# Define the class
class your_module::web_static_config {
  # Install Nginx package
  package { 'nginx':
    ensure => 'installed',
  }

  # Create directories
  file { '/data/web_static/shared':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/test':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  # Create index.html file
  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    content => 'Holberton School',
  }

  # Remove the existing symbolic link if it exists
  file { '/data/web_static/current':
    ensure => 'absent',
  }

  # Create a symbolic link
  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  # Configure Nginx
  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    owner   => 'root',
    group   => 'root',
    source  => 'puppet:///modules/your_module/nginx_config.erb',
    require => Package['nginx'], # Ensure Nginx is installed before applying this config
  }
}
