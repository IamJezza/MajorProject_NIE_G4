module full_adder5(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = a&b|cin&(a|1'b1); 
// initial begin
//     $display("The incorrect adder with or0 having in2/1");
// end   
endmodule