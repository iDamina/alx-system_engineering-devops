#!/usr/bin/puppet
# Install an especific version of flask (2.1.0)
package {'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}