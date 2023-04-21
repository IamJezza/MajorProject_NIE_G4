module incorr_full_adder(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = 1'b0;
assign cout = a&b|cin&(a&b); 
// initial begin
//     $display("The incorrect adder with xor1 having out/0");
// end   
endmodule