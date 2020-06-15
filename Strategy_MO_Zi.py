# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 23:37:23 2020

@author: Lenovo
"""

import os
import sys
import time
import numpy as np
import pandas as pd
sys.path.append(os.path.pardir)
os.chdir("C:\\Users\\Lenovo\\Desktop")

from Simulator import Simulator
import matplotlib.pyplot as plt


DAILY_VOL    = 0.09276              # daily(-->TimeHorizon=100s) volatility
DAILY_VOLUME = 187760              # ADTV
TOTAL_SIZE   = int(DAILY_VOLUME * 0.1)   # shares to execute
EXEC_PERIOD  = 10                   # liquidation period

DIRECTION    = "sell"
ORDER_ID     = "strategy"

class Algo:  # base class
    def __init__(self):
        self.done = False
    
    def reset(self):
        self.__init__()
    
    def action(self, state):
        strategy_order = []
        return strategy_order, self.done


class FinalStrategy(Algo):
    
    __init__base = Algo.__init__
    
    def __init__(self):
        
        self.__init__base()
        self.done  = False
        
    def reset(self):
        
        self.__init__base()
        
    
    def action(self, state):

        if not self.done:

            if state.strategy_record.position > -TOTAL_SIZE:
                if state.bid >= 10.5:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(100, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid >= 10.3 and state.bid < 10.5:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(50, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid > 10.0 and state.bid < 10.3:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(25, abs(state.strategy_record.position+TOTAL_SIZE)), 0]               
                elif state.bid >= 9.8 and state.bid <= 10.0:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(10, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid < 9.8:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(5, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                                
            else:
                self.done = True
                strategy_order = []
        else:
            strategy_order = []
        
        return [strategy_order], self.done
    
class myStrategy2(Algo):
    
    __init__base = Algo.__init__
    
    def __init__(self):
        
        self.__init__base()
        self.done  = False
        
    def reset(self):
        
        self.__init__base()
        
    
    def action(self, state):

        if not self.done:

            if state.strategy_record.position > -TOTAL_SIZE and state.current_time < 0.99*state.time_horizon:
                if state.bid >= 10.5:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(100, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid >= 10.3 and state.bid < 10.5:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(50, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid > 10.0 and state.bid < 10.3:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(25, abs(state.strategy_record.position+TOTAL_SIZE)), 0]               
                elif state.bid >= 9.8 and state.bid <= 10.0:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(10, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid < 9.8:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(0, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
            
            elif state.strategy_record.position > -TOTAL_SIZE and state.current_time >= 0.99*state.time_horizon:
                strategy_order = [ORDER_ID, "market", DIRECTION, abs(state.strategy_record.position+TOTAL_SIZE), 0]
        
                    
            else:
                self.done = True
                strategy_order = []
        else:
            strategy_order = []
        
        return [strategy_order], self.done
    
class myStrategy3(Algo):
    
    __init__base = Algo.__init__
    
    def __init__(self):
        
        self.__init__base()
        self.done  = False
        
    def reset(self):
        
        self.__init__base()
        
    
    def action(self, state):

        if not self.done:

            if state.strategy_record.position > -TOTAL_SIZE and state.current_time <= 0.5*state.time_horizon:
                if state.bid >= 10.5:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(100, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid >= 10.3 and state.bid < 10.5:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(50, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid > 10.0 and state.bid < 10.3:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(25, abs(state.strategy_record.position+TOTAL_SIZE)), 0]               
                elif state.bid >= 9.8 and state.bid <= 10.0:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(10, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid < 9.8:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(0, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
            
            elif state.strategy_record.position > -TOTAL_SIZE and state.current_time > 0.5*state.time_horizon:
                if state.bid >= 10.4:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(200, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid >= 10.2 and state.bid < 10.4:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(100, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid >= 10.0 and state.bid < 10.2:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(50, abs(state.strategy_record.position+TOTAL_SIZE)), 0]  
                elif state.bid >= 9.7 and state.bid < 10.0:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(20, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                elif state.bid < 9.7:
                    strategy_order = [ORDER_ID, "market", DIRECTION, min(5, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
                    
            else:
                self.done = True
                strategy_order = []
        else:
            strategy_order = []
        
        return [strategy_order], self.done
    
    
class BM_Strategy(Algo):
    
    __init__base = Algo.__init__
    
    def __init__(self, k):
        
        self.__init__base()
        '''strategy params'''
        self.k = k
        self.done  = False
        
    def reset(self):
        
        self.__init__base()
        
    
    def action(self, state):

        if not self.done:

            if state.strategy_record.position > -TOTAL_SIZE:
                strategy_order = [ORDER_ID, "market", DIRECTION, min(self.k, abs(state.strategy_record.position+TOTAL_SIZE)), 0]
            else:
                self.done = True
                strategy_order = []
        else:
            strategy_order = []
        
        return [strategy_order], self.done

                        
if __name__ == '__main__':
    
    
    '''
    
    # Benckmark Strategy
    
    ## which strategy to use
    strat = "strategy"
    ## init simulator
    env  = Simulator(strat_name=strat, trans_record=True)
    
    k = 20
    
    Qty = k * [0.0]
    ave_shortfall     = k * [0.0]
    var = k * [0.0]
    ave_time_cost = k * [0.0]
    obj_func = k * [0.0]
    
    for i in range(k):
        if strat == "strategy":
            algo = BM_Strategy(10*(i+1))  
    
        episodes      = 1000
        # episodes      = 100
        shortfall     = episodes * [0.0]
        ref_revenue   = episodes * [0.0]
        strat_revenue = episodes * [0.0]
        time_cost = episodes * [0.0]
    
    
        # time for running program
        RunningStartTime = time.perf_counter()
        for episode in range(episodes):        
            # print(episode)
            # reset state and algos
            state = env.reset(strat_name=strat, trans_record=True)
            algo.reset()
            done = False
            qty_count = 0
            OrderNum = 0
    
            while (state.current_time < state.time_horizon) and not done:
                # run the algorithm for one episode
                algo_action, done = algo.action(state)   
                #OrderNum += 1
                #print(round(state.current_time,3), OrderNum, algo_action)
            
                # state, reward, done, info = env.step(action)
                state = env.step(algo_action)
            
        
            # env.ZIAgent.ZIAgentPirceOrderPlot()
            #env.ZIAgent.PirceTimePlot()
        
            shortfall[episode], ref_revenue[episode], strat_revenue[episode] = env.slippage()
            time_cost[episode] = state.current_time
        
        
        # RunningTime = round(time.perf_counter()-RunningStartTime,3)
        # print(f"the running cost: {RunningTime} seconds")
        result = pd.DataFrame()
        result['shortfall'] = shortfall
        result['ref_revenue'] = ref_revenue
        result['strat_revenue'] = strat_revenue
        result['time_cost'] = time_cost
        # print(result)
        
        Qty[i] = int(round(10*(i+1)))
        ave_shortfall[i] = np.mean(result['shortfall'])
        var[i] = np.var(result['shortfall'])
        obj_func[i] = round(np.mean(result['shortfall']) + 0.0001*np.var(result['shortfall']),2)
        ave_time_cost[i] = np.mean(result['time_cost'])
        
        
    result2 = pd.DataFrame()
    result2['Qty'] = Qty
    result2['ave_shortfall'] = ave_shortfall
    result2['var'] = var
    result2['obj_func'] = obj_func
    result2['ave_time_cost'] = ave_time_cost
    print(result2)
    '''


    '''
    Improved Strategy
    '''
    ## which strategy to use
    strat = "strategy"
    ## init simulator
    env  = Simulator(strat_name=strat, trans_record=True)
    
    if strat == "strategy":
        algo = BM_Strategy(10)
    
    episodes      = 10000
    # episodes      = 100
    shortfall     = episodes * [0.0]
    ref_revenue   = episodes * [0.0]
    strat_revenue = episodes * [0.0]
    time_cost = episodes * [0.0]
    
    # time for running program
    RunningStartTime = time.perf_counter()
    for episode in range(episodes):        
        # print(episode)
        # reset state and algos
        state = env.reset(strat_name=strat, trans_record=True)
        algo.reset()
        done = False
        qty_count = 0
        OrderNum = 0
    
        while (state.current_time < state.time_horizon) and not done:
            # run the algorithm for one episode
            algo_action, done = algo.action(state)   
            #OrderNum += 1
            #print(round(state.current_time,3), OrderNum, algo_action)
            
            # state, reward, done, info = env.step(action)
            state = env.step(algo_action)
            
        
        # env.ZIAgent.ZIAgentPirceOrderPlot()
        #env.ZIAgent.PirceTimePlot()
        
        shortfall[episode], ref_revenue[episode], strat_revenue[episode] = env.slippage()
        time_cost[episode] = state.current_time
        
    RunningTime = round(time.perf_counter()-RunningStartTime,3)
    print(f"the running cost: {RunningTime} seconds")
    result = pd.DataFrame()
    result['shortfall'] = shortfall
    result['ref_revenue'] = ref_revenue
    result['strat_revenue'] = strat_revenue
    result['time_cost'] = time_cost
    
    print(result)
    print(round(np.mean(result['shortfall']) + 0.0001*np.var(result['shortfall']),2))
    print(np.mean(result['shortfall']))
    print(np.var(result['shortfall']))
    print(np.mean(result['time_cost']))
    
    plt.hist(result['shortfall'],bins=1000)
    
    
    
                   
    
    
                      