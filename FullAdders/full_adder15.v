module incorr_full_adder(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = 1'b0|cin&(a|b); 
// initial begin
//     $display("The incorrect adder with and0 and or2 having out/0 and in1/0");
// end   
endmodule