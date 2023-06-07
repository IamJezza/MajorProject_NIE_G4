module full_adder7(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = 1'b0^b^cin;
assign cout = a&b|cin&(a|b); 
// initial begin
//     $display("The incorrect adder with xor0 having in1/0");
// end   
endmodule
