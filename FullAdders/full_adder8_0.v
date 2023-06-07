module full_adder8(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = a&b|cin&(a|b); 
// initial begin
//     $display("The correct adder");
// end   
endmodule