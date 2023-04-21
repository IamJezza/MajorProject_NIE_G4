module incorr_full_adder(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = 1'b1&b|cin&(a|b); 
// initial begin
//     $display("The incorrect adder with and0 having in1/1");
// end   
endmodule