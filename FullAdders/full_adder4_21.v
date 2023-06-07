module full_adder4(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = a&b|cin&(1'b0); 
// initial begin
//     $display("The incorrect adder with or0 and and1 having out/0 and in1/0");
// end   
endmodule