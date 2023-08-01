#!/usr/bin/env ruby
# Define the regular expression pattern

pattern = /School/
argument = ARGV[0]
matches = argument.scan(pattern)
puts matches.join
