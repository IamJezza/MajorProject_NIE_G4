module test_bench;
reg[7:0] A, B;
reg CIN;
wire[8:0] SUM;

wire[6:0] w;
full_adder a1(.a(A[0]), .b(B[0]), .cin(CIN), .sum(SUM[0]), .cout(w[0]));
full_adder a2(.a(A[1]), .b(B[1]), .cin(w[0]), .sum(SUM[1]), .cout(w[1]));
full_adder a3(.a(A[2]), .b(B[2]), .cin(w[1]), .sum(SUM[2]), .cout(w[2]));
full_adder a4(.a(A[3]), .b(B[3]), .cin(w[2]), .sum(SUM[3]), .cout(w[3]));
full_adder a5(.a(A[4]), .b(B[4]), .cin(w[3]), .sum(SUM[4]), .cout(w[4]));
full_adder a6(.a(A[5]), .b(B[5]), .cin(w[4]), .sum(SUM[5]), .cout(w[5]));
full_adder a7(.a(A[6]), .b(B[6]), .cin(w[5]), .sum(SUM[6]), .cout(w[6]));
incorr_full_adder a8(.a(A[7]), .b(B[7]), .cin(w[6]), .sum(SUM[7]), .cout(SUM[8]));

initial begin
    if ($value$plusargs("A=%d", A)) begin
        if ($value$plusargs("B=%d", B)) begin
            if ($value$plusargs("CIN=%b", CIN)) begin
                #0.01 $display("%d",SUM);
            end
        end
    end
end
endmodule
