string data = File.ReadAllText("input.txt");

var dataArray = data.Split("\n").Select(d => int.Parse(d)).ToArray();

for (int i = 0; i < dataArray.Length; i++)
{
    for (int j = i; j < dataArray.Length; j++)
    {
        for (int k = j; k < dataArray.Length; k++)
        {
            if (dataArray[i] + dataArray[j] + dataArray[k] == 2020) { Console.WriteLine(dataArray[i] * dataArray[j] * dataArray[k]); return; }
        }
    }
}