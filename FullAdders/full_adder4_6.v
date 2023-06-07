module full_adder4(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = 1'b1^cin;
assign cout = a&b|cin&(a&b); 
// initial begin
//     $display("The incorrect adder with xor0 and xor1 having out/1 and in1/1");
// end   
endmodule