#!/usr/bin/env ruby
if ARGV[0] =~ /\[from:(.*?)\].*\[to:(.*?)\].*\[flags:(.*?)\]/
  puts "#{$1},#{$2},#{$3}"
end
