module full_adder8(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = a&b|cin&(1'b0|b); 
// initial begin
//     $display("The incorrect adder with or0 having in1/0");
// end   
endmodule