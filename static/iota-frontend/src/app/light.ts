type Tuple = [number, number, number];
export class Light {
  constructor(public l_name: string, public l_rgb: Tuple){
    this.name = l_name;
    this.rgb = l_rgb;
  }
  name: string;
  rgb: Tuple;
}
