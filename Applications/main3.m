function sir
    n = 10^5;
    I0 = 100;
    S0 = n - I0;
    R0 = 0;
    
    [t,x] = ode45(@odept, [0 200], [S0; I0; R0]);
    subplot(1,1,1);
    plot(t, log(x(:,1)))
    hold on
    plot(t, log(x(:,2)))
    plot(t, log(x(:,3)))
    legend('S', 'I', 'R')
    xlabel('t')
    ylabel('log x')
    title('S0R0 = 0.9')
    hold off;
end

function fx = odept(t,x)
    n = 10^5;
    I0 = 100;
    S0 = n - I0;
    gamma = 0.0714286;
    S0R0 = 0.9;
    beta = S0R0 * gamma/S0;
    fx = [-beta*x(1)*x(2); beta*x(1)*x(2) - gamma*x(2); gamma*x(2)];
end