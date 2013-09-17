a = 100
b = "Hello, world"
IT_IS_STATIC = "well"

def sum a , b
	a + b
end  

def min(a, b)
	return a - b 
end 

def work_with_bananas banan , bananas
	if banan == 'string'
		return bananas
	elsif banan == 'int'
		bananas.each { |b| b = b.to_i }
		return bananas
	else
		return nil
	end 
end

def convert_string_to_integer_to_string s
	s.to_i.to_s(2)
end

working_with_bananas = false 

while !lets_check
	puts "do you wanna work with bananas"
	puts "y/n?"
	case gets.chomp 
	when 'y'
		working_with_bananas = true
		lets_check = true
	when 'n'
		working_with_bananas = false
		lets_check = true
	else
		lets_check = false
	end 
		
end


puts b
puts "reading first"
c = gets.chomp
puts "reading second"
d = gets.chomp

unless working_with_bananas
	ar = working_with_bananas 'int', [c,d]
	c = ar[0]
	d = ar[1]	
end


puts "what do you whant to do?"
puts "1) Sum"
puts "2) Min"
puts "3) Dance like a drunken duck"
what_to_do = gets.chomp

case  what_to_do
when "1"
	puts sum c,d 
when "2"
	puts min(c,d)
when "3"
	puts ["Hello", "Boom", "Dance", "Chocken legs"]	
else
	puts "Why would you kill them?"
end 

puts "now lets make some convertion"
puts "we will only make one from decimal to binary"
puts "enter your number"
number = gets.chomp
puts convert_string_to_integer_to_string number

