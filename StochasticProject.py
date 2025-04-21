import math
#test test 
def queuing_model(arrival_rate, service_rate, num_servers=1):
    if num_servers == 1:
        # Handle M/M/1 model
        if arrival_rate >= service_rate:
            return {"error": "Unstable system (λ ≥ μ)"}
        utilizationRate = arrival_rate / service_rate
        P0 = 1 - utilizationRate
        L = arrival_rate / (service_rate - arrival_rate)
        Lq = (arrival_rate ** 2) / (service_rate * (service_rate - arrival_rate))
        W = 1 / (service_rate - arrival_rate)
        Wq = arrival_rate / (service_rate * (service_rate - arrival_rate))
        Pw = utilizationRate
        return {
            "Model": "M/M/1",
            "P0": P0,
            "L": L,
            "Lq": Lq,
            "W": W,
            "Wq": Wq,
            "Pw": Pw,
            "rho": utilizationRate
        }
    else: #M/M/k model

        numberOfServers = num_servers
        if arrival_rate >= numberOfServers * service_rate:
            return {"error": f"Unstable system (λ ≥ {numberOfServers}μ)"}
        utilizationRate = arrival_rate / (numberOfServers * service_rate)
        
        # Compute P0
        sum_part = 0.0
        for n in range(numberOfServers - 1):
            term = ( 1/math.factorial(n) ) * ( (arrival_rate / service_rate) ** n )
            sum_part += term
        last_term = ( (1/math.factorial(numberOfServers)) * (arrival_rate / service_rate) ** numberOfServers )
        last_term *= (numberOfServers * service_rate) / (numberOfServers * service_rate - arrival_rate)
        P0 = 1 / (sum_part + last_term)
        
        # Compute Pw (probability of waiting)
        Pw = ( ( (arrival_rate / service_rate) ** numberOfServers ) / math.factorial(numberOfServers) ) * ( (numberOfServers * service_rate) / (numberOfServers * service_rate - arrival_rate) ) * P0
        
        # Compute Lq
        numerator_Lq = ( (arrival_rate / service_rate) ** numberOfServers ) * arrival_rate * service_rate
        denominator_Lq = math.factorial(numberOfServers - 1) * ( (numberOfServers * service_rate - arrival_rate) ** 2 )
        Lq = ( numerator_Lq / denominator_Lq ) * P0
        
        # Compute other metrics
        L = Lq + (arrival_rate / service_rate)
        Wq = Lq / arrival_rate
        W = Wq + (1 / service_rate)
        
        return {
            "Model": f"M/M/{numberOfServers}",
            "P0": P0,
            "L": L,
            "Lq": Lq,
            "W": W,
            "Wq": Wq,
            "Pw": Pw,
            "rho": utilizationRate
        }

# Example Usage
print("M/M/1 Example:")
print(queuing_model(arrival_rate=2, service_rate=3, num_servers=1))

print("\nM/M/2 Example:")
print(queuing_model(arrival_rate=4, service_rate=3, num_servers=2))
