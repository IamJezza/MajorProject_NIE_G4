module full_adder4(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = 1'b1|cin&(a|b); 
// initial begin
//     $display("The incorrect adder with and0 and or2 having out/1 and in1/1");
// end   
endmodule