module full_adder1(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^1'b1;
assign cout = a&b|cin&(a&b); 
// initial begin
//     $display("The incorrect adder with xor1 having in2/1");
// end   
endmodule