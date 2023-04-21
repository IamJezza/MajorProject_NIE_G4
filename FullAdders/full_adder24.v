module incorr_full_adder(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum = a^b^cin;
assign cout = a&b|1'b1&(a&b); 
// initial begin
//     $display("The incorrect adder with and1 having in1/1");
// end   
endmodule