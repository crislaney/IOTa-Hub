import { Component, OnInit } from '@angular/core';
import { Light } from '../light';
@Component({
  selector: 'app-lights',
  templateUrl: './lights.component.html',
  styleUrls: ['./lights.component.css']
})
export class LightsComponent implements OnInit {


  colorChange(val: number) {
    var val_hex_string: string = val.toString(16);
    console.log(val.toString(16));
    var red: string = val_hex_string.substring(0,2);
    var green: string = val_hex_string.substring(2, 4);
    var blue: string = val_hex_string.substring(4, 7);

    
  }

  briChange(val: number) {
    console.log("Slider changed!");
    console.log(val)
  };

  satChange(val: number) {
    console.log("Slider changed!");
    console.log(val)
  };
  light1: Light = {
    id: 5,
    name: "Cris Bedroom 1",
    xy:[0.004, 0.05]
  };

  constructor() { }

  ngOnInit() {
  }

}
