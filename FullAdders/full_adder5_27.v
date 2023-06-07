module full_adder5(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = 1'b0; 
// initial begin
//     $display("The incorrect adder with or1 having out/0");
// end   
endmodule