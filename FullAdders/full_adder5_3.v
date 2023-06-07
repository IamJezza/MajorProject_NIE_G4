module full_adder5(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^1'b0^cin;
assign cout = a&b|cin&(a&b); 
// initial begin
//     $display("The incorrect adder with xor0 having in2/0");
// end   
endmodule