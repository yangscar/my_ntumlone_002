syms u v

f = symfun(exp(u)+exp(2*v)+exp(u*v)+u^2-2*u*v+2*v^2-3*u-2*v,[u,v]);
diff_u = diff(f,u);
diff_v = diff(f,v);

uv = [0 0];
eta = 0.01;
for i = 1:5
    uv = uv - eta.*[eval(subs(diff_u,[u,v],uv)),...
                    eval(subs(diff_v,[u,v],uv))];
end

fprintf('%.3f %.3f\n',uv);
fprintf('E(u5,v5) = %.3f\n',eval(subs(f,[u,v],uv)));