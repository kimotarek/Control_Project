package com.example.demo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;

@Component
@RestController
@CrossOrigin

public class Controller {
    @ResponseBody
    @RequestMapping(value = "/addshape/{s}/{e}",method = RequestMethod.POST)
    public ArrayList<ArrayList<String>> addShape(@RequestBody int[][] g, @PathVariable int s, @PathVariable int e) {
        System.out.print("[");
        for(int i = 0; i <= e; i++)
        {
            System.out.print("[");
            for(int j = 0; j <= e; j++)
            {
                System.out.print(g[i][j]);
                if(j!=e)
                    System.out.print(", ");
            }
            System.out.println("]");
        }
        System.out.println("]");
        Graph graph = new Graph(g);
        return graph.solve(s, e);
    }

}
