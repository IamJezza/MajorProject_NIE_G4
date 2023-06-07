module full_adder5(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = a&b|1'b0&(a&b); 
// initial begin
//     $display("The incorrect adder with and1 having in1/0");
// end   
endmodule