def apply_operation(left_operand, right_operand, operator):
   return eval(str(left_operand)+operator+str(right_operand))

print(apply_operation(2,3,'+'))
