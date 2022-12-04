using System.Security.Cryptography.MD5 md5 = System.Security.Cryptography.MD5.Create();

string puzInput = "yzbqklnj";

int x = 1;
while (true)
{
    string newString = puzInput + x.ToString();
    byte[] inputBytes = System.Text.Encoding.ASCII.GetBytes(newString);
    byte[] hashBytes = md5.ComputeHash(inputBytes);

    if (Convert.ToHexString(hashBytes).Substring(0, 6) == "000000") { Console.WriteLine(newString); Console.WriteLine(Convert.ToHexString(hashBytes)); return; }
    x += 1;
}