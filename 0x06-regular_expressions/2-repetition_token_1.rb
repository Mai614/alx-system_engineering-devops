#!/usr/bin/env ruby
# regular expression that will match the pattern
puts ARGV[0].scan(/^hb{0,1}tn$/).join
