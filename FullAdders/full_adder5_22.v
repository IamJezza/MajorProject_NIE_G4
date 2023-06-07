module full_adder5(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = a&b|cin&(1'b1); 
// initial begin
//     $display("The incorrect adder with or0 and and1 having out/1 and in1/1");
// end   
endmodule