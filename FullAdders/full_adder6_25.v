module full_adder6(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = a&b|1'b0; 
// initial begin
//     $display("The incorrect adder with and1 and or1 having out/0 and in2/0");
// end   
endmodule