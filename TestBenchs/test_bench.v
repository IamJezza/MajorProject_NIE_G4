module test_bench;
reg[7:0] A, B;
reg CIN;
wire[8:0] SUM;

wire[6:0] w;
full_adder1 a1(.a(A[0]), .b(B[0]), .cin(CIN), .sum(SUM[0]), .cout(w[0]));
full_adder2 a2(.a(A[1]), .b(B[1]), .cin(w[0]), .sum(SUM[1]), .cout(w[1]));
full_adder3 a3(.a(A[2]), .b(B[2]), .cin(w[1]), .sum(SUM[2]), .cout(w[2]));
full_adder4 a4(.a(A[3]), .b(B[3]), .cin(w[2]), .sum(SUM[3]), .cout(w[3]));
full_adder5 a5(.a(A[4]), .b(B[4]), .cin(w[3]), .sum(SUM[4]), .cout(w[4]));
full_adder6 a6(.a(A[5]), .b(B[5]), .cin(w[4]), .sum(SUM[5]), .cout(w[5]));
full_adder7 a7(.a(A[6]), .b(B[6]), .cin(w[5]), .sum(SUM[6]), .cout(w[6]));
full_adder8 a8(.a(A[7]), .b(B[7]), .cin(w[6]), .sum(SUM[7]), .cout(SUM[8]));

initial begin
    if ($value$plusargs("A=%d", A)) begin
        if ($value$plusargs("B=%d", B)) begin
            if ($value$plusargs("CIN=%b", CIN)) begin
                #1 $display("%d",SUM);
            end
        end
    end
end
endmodule
