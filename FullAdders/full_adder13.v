module incorr_full_adder(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = a&1'b0|cin&(a|b); 
// initial begin
//     $display("The incorrect adder with and0 having in2/0");
// end   
endmodule