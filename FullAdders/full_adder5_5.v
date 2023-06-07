module full_adder5(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = 1'b0^cin;
assign cout = a&b|cin&(a&b); 
// initial begin
//     $display("The incorrect adder with xor0 and xor1 having out/0 and in1/0");
// end   
endmodule