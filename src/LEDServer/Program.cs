using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Raspberry.IO.GeneralPurpose;
using Raspberry.IO.GeneralPurpose.Behaviors;

namespace LEDServer
{
  public static class Program
  {
    public static void Main(string[] args)
    {
      var driver = new GpioConnectionDriver();
    }
  }
}
